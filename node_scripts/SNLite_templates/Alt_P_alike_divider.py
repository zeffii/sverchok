"""
in   verts  v   .=[]   n=0
in   faces  s   .=[]   n=0
in   scale  s   .=0.0  n=0
out  overts   v
out  ofaces   s
"""

from mathutils import Vector as V
from mathutils.geometry import normal as nm
import numpy as np

Verts = []
Edges = []

for ov, of in zip(verts, faces):
    lv = len(ov)
    overts_ = ov
    ofaces_ = []
    fcs = []
    for f in of:
        vrts = [ov[i] for i in f]
        norm = nm(V(ov[f[0]]),V(ov[f[1]]),V(ov[f[2]]))
        nv  = np.array(vrts)
        vrt  = (nv.sum(axis=0)/len(f))+np.array(norm*scale)
        fcs = [[i,k,lv] for i,k in zip(f,f[-1:]+f[:-1])]
        overts_.append(vrt.tolist())
        ofaces_.extend(fcs)
        lv += 1
    overts.append(overts_)
    ofaces.append(ofaces_)