import matplotlib.pyplot as plt
import numpy as np


x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

# Colormap in the scatter, marks on the bar
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
plt.scatter(x, y, c=colors, cmap='viridis', s=19, marker='s', alpha=0.6, edgecolors='face')
plt.xlabel('X')
plt.ylabel('Y')
# Display the color bar
plt.colorbar()
plt.show()

# List of parameters that can be applied:

# x, y      --> Data type: float or array like

# c         --> Data type: array-like or list of colors or color, opt
#               List of possible values:
#               ["red","green","blue","yellow","pink","black","orange",
#               "purple","beige","brown","gray","cyan","magenta"]

# marker    --> Data type: char
#               The marker style. marker can be either an instance of the class or the text shorthand for a particular marker.
#               Possible values:
#               'o' - default, 's' - squares, '+', .....

# cmap      --> Data type: 'String'
#               A Colormap instance or registered colormap name.

# norm      --> Data type: default=None
#               If c is an array of floats, norm is used to scale the color data, c, in the range 0 to 1,
#               in order to map into the colormap cmap. If None, use the default

# vmin, vmax--> Data type: float, default: None
#               vmin and vmax are used in conjunction with the default norm to map the color array c to the colormap cmap.
#               If None, the respective min and max of the color array is used.

# alpha     --> Data type: float, default=None
#               The alpha blending value, between 0 (transparent) and 1 (opaque).

# s         --> Data type: float or array-like
#               Setting the size of the dots with the s argument.

# linewidths--> Values: float or array-like
#               The linewidth of the marker edges. Note: The default edgecolors is 'face'. You may want to change this as well.

# edgecolors --> Values: 'face', 'none', 'None'
#                The edge color of the marker.
#                'face': The edge color will always be the same as the face color.
#                'none': No patch boundary will be drawn.
#                Default - A color or sequence of colors.
# plotnonfinite --> Data type: bool, default:False
#                   Set to plot points with nonfinite c, in conjunction with set_bad.


# Most useful parameters: marker, alpha, s - size, c - color,


