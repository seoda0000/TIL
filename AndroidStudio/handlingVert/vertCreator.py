import os


def obj_to_vert(obj_path, vert_path):
    with open(obj_path, 'r') as obj_file, open(vert_path, 'w') as vert_file:
        vertices = []
        normals = []
        texcoords = []
        indices = []
        index_offset = 0

        for line in obj_file:
            if line.startswith('v '):
                vertex = list(map(float, line.split()[1:]))
                vertices.append(vertex)
            elif line.startswith('vn '):
                normal = list(map(float, line.split()[1:]))
                normals.append(normal)
            elif line.startswith('vt '):
                texcoord = list(map(float, line.split()[1:]))
                texcoords.append(texcoord)
            elif line.startswith('f '):
                face = line.split()[1:]
                if len(face) == 3:
                    for i in range(3):
                        vertex_index, texcoord_index, normal_index = [int(index) - 1 for index in face[i].split('/')]
                        vertex = vertices[vertex_index]
                        texcoord = texcoords[texcoord_index] if texcoord_index >= 0 else [0, 0]
                        normal = normals[normal_index] if normal_index >= 0 else [0, 0, 0]
                        indices.append(vertex_index + index_offset)
                        vert_file.write(
                            f"{vertex[0]} {vertex[1]} {vertex[2]} {normal[0]} {normal[1]} {normal[2]} {texcoord[0]} {texcoord[1]}\n")
                elif len(face) == 4:
                    for i in range(3):
                        vertex_index, texcoord_index, normal_index = [int(index) - 1 for index in face[i].split('/')]
                        vertex = vertices[vertex_index]
                        texcoord = texcoords[texcoord_index] if texcoord_index >= 0 else [0, 0]
                        normal = normals[normal_index] if normal_index >= 0 else [0, 0, 0]
                        indices.append(vertex_index + index_offset)
                        vert_file.write(
                            f"{vertex[0]} {vertex[1]} {vertex[2]} {normal[0]} {normal[1]} {normal[2]} {texcoord[0]} {texcoord[1]}\n")
                    for i in range(2, 5):
                        vertex_index, texcoord_index, normal_index = [int(index) - 1 for index in face[i].split('/')]
                        vertex = vertices[vertex_index]
                        texcoord = texcoords[texcoord_index] if texcoord_index >= 0 else [0, 0]
                        normal = normals[normal_index] if normal_index >= 0 else [0, 0, 0]
                        indices.append(vertex_index + index_offset)
                        vert_file.write(
                            f"{vertex[0]} {vertex[1]} {vertex[2]} {normal[0]} {normal[1]} {normal[2]} {texcoord[0]} {texcoord[1]}\n")
                    index_offset += 3

        vert_file.write('\n'.join([str(i) for i in indices]))


if __name__ == '__main__':
    obj_path = 'Devil_Tree_Candy.obj'
    vert_path = 'Devil_Tree_Candy.vert'
    obj_to_vert(obj_path, vert_path)
