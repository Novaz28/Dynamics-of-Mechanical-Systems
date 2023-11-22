from mpl_toolkits.mplot3d import Axes3D

class InertialFrame:
    def __init__(self, origin, x_axis, y_axis, z_axis):
        self.origin = origin
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.z_axis = z_axis

# Example usage
origin = (0, 0, 0)
x_axis = (1, 0, 0)
y_axis = (0, 1, 0)
z_axis = (0, 0, 1)

inertial_frame = InertialFrame(origin, x_axis, y_axis, z_axis)
import matplotlib.pyplot as plt

# Create a figure and a 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Get the origin and axes vectors from the inertial frame
origin = inertial_frame.origin
x_axis = inertial_frame.x_axis
y_axis = inertial_frame.y_axis
z_axis = inertial_frame.z_axis

# Plot the origin
ax.scatter(*origin, color='red', label='Origin')

# Plot the x-axis
ax.quiver(*origin, *x_axis, color='blue', label='X-Axis')

# Plot the y-axis
ax.quiver(*origin, *y_axis, color='green', label='Y-Axis')

# Plot the z-axis
ax.quiver(*origin, *z_axis, color='orange', label='Z-Axis')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Inertial Frame')

# Set the aspect ratio to 'equal'
ax.set_box_aspect([1, 1, 1])

# Add a legend
ax.legend()

# Show the plot
plt.show()

