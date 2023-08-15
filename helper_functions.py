import matplotlib.pyplot as plt


def make_vector(images):
    return X.reshape((-1, 58*50))

def split_vector(image_vec):
    return image_vec.reshape((-1,58,50))