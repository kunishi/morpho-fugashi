import os
import sys
import pathlilb
import argparse
from fugashi import Tagger

parser = argparse.ArgumentParser()
parser.add_argument("indir")
parser.add_argument("outdir")
args = parser.parse_args()

tagger = Tagger('-Owakati')

datadir = pathlib.Path(args.indir)
outdir = args.outdir
if not os.path.exists(outdir):
    os.makedirs(outdir)
for file in datadir.glob('[A-Z]/wiki_*'):
    with open(file, 'r') as f:
        text = f.read()
    words = tagger.parse(text)
    p_file = pathlib.Path(file)
    outfile = os.path.join(outdir, '_'.join([p_file.parent.stem, p_file.name]))
    with open(outfile, 'w') as f:
        print(outfile)
        f.write(' '.join(words))
        

