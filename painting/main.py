import colorgram

# Extract all colors from an image.
colors = colorgram.extract('image.jpg', 110)

# Create an empty list to store RGB tuples.
rgb_tuples = []

# Loop through all colors and append their RGB tuples to the list.
for color in colors:
    # Get the RGB values of the color.
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    # Create a tuple of the RGB values.
    new_color = (r, g, b)

    # Add the new color tuple to the list.
    rgb_tuples.append(new_color)
import colorgram

# Extract all colors from an image.
colors = colorgram.extract('image.jpg', 110)

# Create an empty list to store RGB tuples.
rgb_tuples = []

# Loop through all colors and append their RGB tuples to the list.
for color in colors:
    # Get the RGB values of the color.
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    # Create a tuple of the RGB values.
    new_color = (r, g, b)

    # Add the new color tuple to the list.
    rgb_tuples.append(new_color)

# Print the list of RGB tuples.
print(rgb_tuples)

# Manually created list of painting colors.
colors_painting = [(250, 246, 243), (248, 245, 246), (212, 154, 97), (239, 246, 243), (52, 108, 132), (178, 78, 33),
                   (198, 143, 34), (123, 80, 97), (235, 240, 244), (116, 155, 171), (124, 175, 158), (228, 197, 129),
                   (194, 85, 105), (54, 38, 20), (12, 51, 65), (189, 123, 142), (54, 120, 115), (41, 169, 126),
                   (167, 21, 31), (225, 94, 78), (4, 30, 28), (39, 32, 34), (243, 163, 159), (81, 148, 168),
                   (164, 27, 22), (239, 163, 167), (104, 123, 159), (164, 209, 193), (21, 81, 93), (29, 85, 81),
                   (162, 206, 212), (53, 62, 81), (183, 190, 206), (85, 74, 35)]

# Print the list of RGB tuples.
print(rgb_tuples)

# Manually created list of painting colors.
colors_painting = [(250, 246, 243), (248, 245, 246), (212, 154, 97), (239, 246, 243), (52, 108, 132), (178, 78, 33),
                   (198, 143, 34), (123, 80, 97), (235, 240, 244), (116, 155, 171), (124, 175, 158), (228, 197, 129),
                   (194, 85, 105), (54, 38, 20), (12, 51, 65), (189, 123, 142), (54, 120, 115), (41, 169, 126),
                   (167, 21, 31), (225, 94, 78), (4, 30, 28), (39, 32, 34), (243, 163, 159), (81, 148, 168),
                   (164, 27, 22), (239, 163, 167), (104, 123, 159), (164, 209, 193), (21, 81, 93), (29, 85, 81),
                   (162, 206, 212), (53, 62, 81), (183, 190, 206), (85, 74, 35)]
