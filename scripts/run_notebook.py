"""Execute the analysis from a fresh kernel; retain only aggregate public outputs."""
from pathlib import Path
import base64
import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]

def main():
    path = ROOT / 'notebooks' / 'nft_analysis.ipynb'
    notebook = nbformat.read(path, as_version=4)
    client = NotebookClient(notebook, timeout=3600, kernel_name='python3',
                            resources={'metadata': {'path': str(ROOT)}})
    def progress(cell, cell_index, **kwargs):
        if cell.cell_type == 'code':
            print(f'Executing cell {cell_index + 1}/{len(notebook.cells)}', flush=True)
    client.on_cell_start = progress
    client.execute()
    # Remove row-level previews from the distributable notebook.
    private_previews = ('model_df.head()', 'model_data.head()',
                        'model_data[["transaction_value"', 'outliers[',
                        'enhanced_data[\n')
    figure_dir = ROOT / 'reports' / 'figures'
    figure_dir.mkdir(parents=True, exist_ok=True)
    figure_no = 0
    for cell in notebook.cells:
        if cell.cell_type != 'code':
            continue
        if any(term in cell.source for term in private_previews):
            cell.outputs = []
        for output in cell.outputs:
            png = output.get('data', {}).get('image/png')
            if png:
                figure_no += 1
                (figure_dir / f'figure_{figure_no:02}.png').write_bytes(base64.b64decode(png))
    nbformat.write(notebook, path)
    print(f'Completed: {len(notebook.cells)} cells, {figure_no} figures.', flush=True)

if __name__ == '__main__':
    main()
