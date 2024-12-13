from molpub import DefaultStructureImage, Figure, HighlightStructureImage


def baseline(file_parent_path, save_parent_path):
    # Initial visualization of the structures in case.
    for structure_name in ["GPR110Gq", "GPR110Gs", "GPR110G12", "GPR110G13", "GPR110Gi"]:
        origin_structure = DefaultStructureImage(structure_paths=[file_parent_path + structure_name + ".pdb"])
        origin_structure.save(save_path=save_parent_path + "4." + structure_name + ".png", width=1280)


def designed(file_parent_path, temp_parent_path, save_parent_path):
    # Visualization of the structure GPR110Gq.
    gpr110gq = HighlightStructureImage(structure_paths=[file_parent_path + "GPR110Gq.pdb"])
    gpr110gq.set_state(rotate=[180, 15, 90])
    gpr110gq.set_shape(representation_plan=[("all", "cartoon")])
    gpr110gq.set_color(coloring_plan=[("chain:A", "0x00BFFF"), ("chain:B", "0x8A2BE2"), ("chain:G", "0xFFA54F"),
                                      ("chain:N", "0x00CD00"), ("chain:R", "0x0000EE")])
    gpr110gq.save(save_path=temp_parent_path + "GPR110Gq-cartoon.png", width=1280, ratio=1.0)
    gpr110gq.set_shape(representation_plan=[("all", "surface")])
    gpr110gq.save(save_path=temp_parent_path + "GPR110Gq-surface.png", width=1280, ratio=1.0)
    gpr110gq.close()

    # Visualization of the structure GPR110Gs.
    gpr110gs = HighlightStructureImage(structure_paths=[file_parent_path + "GPR110Gs.pdb"])
    gpr110gs.set_state(rotate=[0, 15, 90])
    gpr110gs.set_shape(representation_plan=[("all", "cartoon")])
    gpr110gs.set_color(coloring_plan=[("chain:A", "0xCD3700"), ("chain:B", "0x8A2BE2"), ("chain:C", "0xFFA54F"),
                                      ("chain:D", "0x00CD00"), ("chain:R", "0x0000EE")])
    gpr110gs.save(save_path=temp_parent_path + "GPR110Gs-cartoon.png", width=1280, ratio=1.0)
    gpr110gs.set_shape(representation_plan=[("all", "surface")])
    gpr110gs.save(save_path=temp_parent_path + "GPR110Gs-surface.png", width=1280, ratio=1.0)
    gpr110gs.close()

    # Visualization of the structure GPR110G12.
    gpr110g12 = HighlightStructureImage(structure_paths=[file_parent_path + "GPR110G12.pdb"])
    gpr110g12.set_state(rotate=[30, 345, 135])
    gpr110g12.set_shape(representation_plan=[("all", "cartoon")])
    gpr110g12.set_color(coloring_plan=[("chain:A", "0xFFB5C5"), ("chain:B", "0x8A2BE2"), ("chain:C", "0x00EE00"),
                                       ("chain:E", "0xFFA54F"), ("chain:R", "0x0000EE")])
    gpr110g12.save(save_path=temp_parent_path + "GPR110G12-cartoon.png", width=1280, ratio=1.0)
    gpr110g12.set_shape(representation_plan=[("all", "surface")])
    gpr110g12.save(save_path=temp_parent_path + "GPR110G12-surface.png", width=1280, ratio=1.0)
    gpr110g12.close()

    # Visualization of the structure GPR110G13.
    gpr110g13 = HighlightStructureImage(structure_paths=[file_parent_path + "GPR110G13.pdb"])
    gpr110g13.set_state(rotate=[330, 0, 315])
    gpr110g13.set_shape(representation_plan=[("all", "cartoon")])
    gpr110g13.set_color(coloring_plan=[("chain:A", "0xEE30A7"), ("chain:B", "0x8A2BE2"), ("chain:C", "0x00EE00"),
                                       ("chain:D", "0xFFA54F"), ("chain:R", "0x0000EE")])
    gpr110g13.save(save_path=temp_parent_path + "GPR110G13-cartoon.png", width=1280, ratio=1.0)
    gpr110g13.set_shape(representation_plan=[("all", "surface")])
    gpr110g13.save(save_path=temp_parent_path + "GPR110G13-surface.png", width=1280, ratio=1.0)
    gpr110g13.close()

    # Visualization of the structure GPR110Gi.
    gpr110gi = HighlightStructureImage(structure_paths=[file_parent_path + "GPR110Gi.pdb"])
    gpr110gi.set_state(rotate=[165, 0, 315])
    gpr110gi.set_shape(representation_plan=[("all", "cartoon")])
    gpr110gi.set_color(coloring_plan=[("chain:B", "0xB0E2FF"), ("chain:C", "0x8A2BE2"), ("chain:E", "0x00EE00"),
                                      ("chain:D", "0xFFA54F"), ("chain:R", "0x0000EE")])
    gpr110gi.save(save_path=temp_parent_path + "GPR110Gi-cartoon.png", width=1280, ratio=1.0)
    gpr110gi.set_shape(representation_plan=[("all", "surface")])
    gpr110gi.save(save_path=temp_parent_path + "GPR110Gi-surface.png", width=1280, ratio=1.0)
    gpr110gi.close()

    # Construct the case figure.
    case = Figure(manuscript_format="Science", occupied_columns=2, aspect_ratio=(1.54, 5), mathtext=False)
    for order, structure_name in enumerate(["GPR110Gq", "GPR110Gs", "GPR110G12", "GPR110G13", "GPR110Gi"]):
        case.set_image(image_path=temp_parent_path + structure_name + "-surface.png", layout=(5, 1, order + 1))
        case.set_image(image_path=temp_parent_path + structure_name + "-cartoon.png",
                       locations=[(0.11 + order * 0.2), 0.45, 0.11, 0.5], transparent=True)
        case.set_text(annotation="G$_{" + structure_name[7::] + "}$", locations=[(0.1 + order * 0.2), 0.1, 0.2, 0.2],
                      font_size=8, weight="bold", transparent=True)
    text_dict = {1: ("GPR110", [0.1, 0.85, 0.2, 0.2], "0000EE"), 2: ("Gα$_{q}$", [0.04, 0.57, 0.2, 0.2], "00BFFF"),
                 3: ("Nb35", [0.05, 0.23, 0.2, 0.2], "00CD00"), 4: ("Gβ", [0.12, 0.19, 0.2, 0.2], "8A2BE2"),
                 5: ("Gγ", [0.16, 0.26, 0.2, 0.2], "FFA54F"), 6: ("Gα$_{s}$", [0.23, 0.56, 0.2, 0.2], "CD3700"),
                 7: ("Gα$_{12}$", [0.41, 0.52, 0.2, 0.2], "FFB5C5"), 8: ("scFv16", [0.57, 0.27, 0.2, 0.2], "00EE00"),
                 9: ("Gα$_{13}$", [0.61, 0.53, 0.2, 0.2], "EE30A7"), 10: ("Gα$_{i}$", [0.81, 0.51, 0.2, 0.2], "B0E2FF")}
    for _, content in text_dict.items():
        case.set_text(annotation=content[0], locations=content[1], font_size=7, weight="bold", color="#" + content[2],
                      transparent=True)
    case.save_figure(save_parent_path + "4.png")


if __name__ == "__main__":
    baseline(file_parent_path="./molecule/4/", save_parent_path="./baseline/")
    designed(file_parent_path="./molecule/4/", temp_parent_path="./temp/", save_parent_path="./designed/")
