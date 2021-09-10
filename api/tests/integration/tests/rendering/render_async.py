import sys

sys.path.append('../../common')
from env_indigo import Indigo, IndigoRenderer

import concurrent.futures

SMILES_LIST = [
    'C',
    'CC',
    'CCC',
    'CCCCC',
    'CCCCCC',
    'CCCCCCC',
    'CCCCCCCC',
]


def render(smiles):
    ind = Indigo()
    imol = ind.loadMolecule(smiles)
    renderer = IndigoRenderer(ind)
    ind.setOption('render-output-format', 'png')
    buff = renderer.renderToBuffer(imol)
    return buff.tobytes()


with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    futures_dict = {
        executor.submit(render, smiles): smiles
        for smiles in SMILES_LIST
    }
    for future in concurrent.futures.as_completed(futures_dict):
        smi = futures_dict[future]
        try:
            data = future.result()
        except Exception as exc:
            print(exc)
        else:
            print(data)
