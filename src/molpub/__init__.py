import os

from matplotlib import font_manager

from molpub.handles import (
    Monitor,
    Score,
    align,
    cluster,
    kmer,
    load_structure_from_file,
    save_structure_to_file,
    set_difference,
    set_properties,
    similar,
)
from molpub.layouts import (
    DefaultStructureImage,
    Figure,
    HighlightStructureImage,
    PropertyStructureImage,
    obtain_widget_icon,
)

# load required font formats.
font_files = font_manager.findSystemFonts(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts"))
for font_file in font_files:
    font_manager.fontManager.addfont(font_file)

__all__ = [
    "DefaultStructureImage",
    "PropertyStructureImage",
    "HighlightStructureImage",
    "obtain_widget_icon",
    "Figure",
    "Monitor",
    "Score",
    "similar",
    "cluster",
    "align",
    "set_properties",
    "set_difference",
    "kmer",
    "load_structure_from_file",
    "save_structure_to_file",
]
