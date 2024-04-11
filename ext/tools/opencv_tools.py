import cv2
import numpy as np

# -------------------------------
def extract_masked_points(image_mask, mask_value=255) -> set:
    """Extracts masked location as a set
  
Args:
    image_mask (nparray or cvimage): 2d nparray of integers 
    mask_value (bool): the value representing the mask
Returns:
    list: a list of points (tuples of (row, col)) of the mask
"""
    #data = np.array(image_mask)[:,:,0]
    wpoint = np.where(image_mask == mask_value)
    points = set((row, col) for row, col in zip(*wpoint)) # (row, col)
    return points

# --- INTERNAL USE: generating the index of the 8 neighours of a pixel
def generate_neighbours(point):
    """
    
    :private:
    """
    neighbours = [ (1, -1), (1, 0),(1, 1),(0, -1), (0, 1), (1, -1), (1, 0),(-1, 1) ]
    for neigh in neighbours:
        yield tuple(map(sum, zip(point, neigh)))
        
# ---- extract the connected region starting from a seed point
def extract_region(seed, points): 
    """Gather a connected region from the points of mask, starting from the seed
    
Args:
    image_mask (nparray or cvimage): 2d nparray of integers 
    mask_value (bool): the value representing the mask
Returns:
    list: a list of points (tuples of (row, col)) of the mask
"""
    region_points = []   # in (row, col)
    seen_points = set()
    the_seeds = [seed]
    while len(the_seeds) > 0:
        point = the_seeds.pop()
        if point not in seen_points:
            seen_points.add(point)
            if point in points:
                region_points.append(point)               
                points.remove(point)
                for n in generate_neighbours(point):
                    the_seeds.append(n)
    region_points = np.asarray(region_points)
    min_point = np.min(region_points, axis=0)
    max_point = np.max(region_points, axis=0)
    bbox = np.hstack((min_point, max_point)) # bbox is a nparray
    return region_points, bbox

# ---- return the score of similarity between two masks
def compare_masks(mask1, mask2) -> float:
    """ Find the similarity of two marks

    :param mask1: The first mark image for comparison
    :type mask1: np.array
    :param mask2: The second mark image for comparison
    :type mask2: np.array
    :return: The similarity score
    :rtype: float
    """
    drow, dcol = min(mask1.shape[0], mask2.shape[0]), min(mask1.shape[1], mask2.shape[1])
    score = (mask1[:drow, :dcol] == mask2[:drow, :dcol]).sum() / (drow * dcol)
    return score

# ---- create a new image of shape (row, col) and copy the mask referenced at the center
def copy_and_pad(mask, row:int, col:int) -> np.array:
    """ Create a new image of shape (row, col) and copy the mask referenced at the center

    :param mask: The source mask image
    :type mask: np.array
    :param row: The number of rows in the new image
    :type row: int
    :param col: The number of columns in the new image
    :type col: int
    :return: The new image
    :rtype: np.array
    """
    assert(row >= mask.shape[0] and col >= mask.shape[1])
    r = (row - mask.shape[0]) // 2
    c = (col - mask.shape[1]) // 2 
    image = np.zeros(shape=(row, col))
    image[r:r+mask.shape[0], c:c+mask.shape[1]] = mask
    return image.astype(np.bool)             

