"""
A few utility functions.
"""
import os
import numpy as np

def to_rgb(I, do_cpy=True):
    """ Convert input image into RGB (color). """
    if len(I.shape) == 3:
        if do_cpy:
            return I.copy()
        else:
            return I
    out = np.zeros([I.shape[0], I.shape[1], 3])
    out[:,:,0] = I
    out[:,:,1] = I
    out[:,:,2] = I
    return out

def intrnd(*args):
    if len(args) == 1:
        return int(round(args[0]))
    else:
        return [int(round(x)) for x in args]

def tupint(thing):
    """ Converts a thing of numbers to a tuple of ints (usually used
    for cv2 functions that *require* tuples of ints.
    """
    return tuple([intrnd(x) for x in thing])

def isimgext(path):
    p = path.lower()
    return p.endswith('.png') or p.endswith('.jpeg') or p.endswith('.jpg') or p.endswith('.bmp')

def get_imgpaths(imgsdir, n=None):
    """ Outputs all imagepaths in imgsdir. Limit to first n if given. """
    imgpaths = []
    for dirpath, dirnames, filenames in os.walk(imgsdir):
        for f in [f for f in sorted(filenames) if isimgext(f)]:
            if (n != None) and (len(imgpaths) == n):
                return imgpaths
            imgpaths.append(os.path.join(dirpath, f))
    return imgpaths

def get_filename(fpath):
    return os.path.splitext(os.path.split(fpath)[1])[0]
