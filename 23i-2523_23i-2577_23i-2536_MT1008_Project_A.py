import sympy as sp  # Importing SymPy library for symbolic mathematics
import numpy as np  # Importing NumPy library for numerical computations
import matplotlib.pyplot as plt  # Importing matplotlib library for plotting
from mpl_toolkits.mplot3d import Axes3D  # Importing Axes3D module for 3D plotting

# Initialize pretty printing for SymPy
sp.init_printing()

# Define the variables for the box dimensions
x, y, z = sp.symbols('x y z', real=True, positive=True)

# Taking inputs from the user
box_weight_capacity = int(input("Enter the Box weight capacity: "))  # Requesting box weight capacity from the user
num_items = int(input("Enter the Number of Items: "))  # Requesting the number of items from the user

items = []  # Initializing an empty list to store item details
total_weight = 0  # Initializing total weight of items to 0
total_volume = 0  # Initializing total volume of items to 0

# Flag to control the input loop
isFalse = False  
while not isFalse:
    # Loop to iterate over each item and get its weight and volume
    for i in range(num_items):
        weight = int(input("Enter the weight of item " + str(i+1) + ": "))  # Requesting weight of each item
        volume = int(input("Enter the volume of item " + str(i+1) + ": "))  # Requesting volume of each item
        total_weight += weight  # Adding weight of current item to total weight
        total_volume += volume  # Adding volume of current item to total volume
        items.append((weight, volume))  # Storing weight and volume of item as a tuple in the list
        
    # Checking if the total weight of items is within box weight capacity
    if box_weight_capacity - total_weight >= 0:  
        isFalse = True  # If yes, exit the loop
    else:
        print("Weight capacity exceeded, please provide correct inputs!!!")  # If not, prompt the user to provide correct inputs
        total_weight = 0  # Reset total weight to 0
        total_volume = 0  # Reset total volume to 0
        items.clear()  # Clear the list of items

# Define the function to optimize and the constraints
f = 2*x*y + 2*x*z + 2*y*z  # Function representing the surface area of the box
g1 = x*y*z - total_volume  # Constraint representing the total volume of items

# Define the Lagrange multiplier
n = sp.symbols('n', real=True)

# Define the Lagrange function
L = f - n * g1
 
# Calculate the partial derivatives
eq1 = sp.diff(L, x)  # Partial derivative with respect to x
eq2 = sp.diff(L, y)  # Partial derivative with respect to y
eq3 = sp.diff(L, z)  # Partial derivative with respect to z
eq4 = g1  # The constraint equation

# Solve the system of equations
solution = sp.solve([eq1, eq2, eq3, eq4], [x, y, z, n], dict=True)

# Display the real solutions
for sol in solution:
    if all(value.is_real for value in sol.values()):
        x_val = sol[x].evalf()  # Evaluate x
        y_val = sol[y].evalf()  # Evaluate y
        z_val = sol[z].evalf()  # Evaluate z
        lambda_val = sol[n].evalf()  # Evaluate lambda
        print(f"Solution:\nx = {x_val}\ny = {y_val}\nz = {z_val}\nn = {lambda_val}")

        # Plot the main storage box (edges only)
        fig_main = plt.figure()
        ax_main = fig_main.add_subplot(111, projection='3d')

        # Define the vertices of the main box
        main_box_vertices = np.array([[0, 0, 0], [x_val, 0, 0], [x_val, y_val, 0], [0, y_val, 0],
                                      [0, 0, z_val], [x_val, 0, z_val], [x_val, y_val, z_val], [0, y_val, z_val]])

        # Define the edges of the main box
        main_box_edges = [
            [main_box_vertices[0], main_box_vertices[1], main_box_vertices[2], main_box_vertices[3], main_box_vertices[0]],
            [main_box_vertices[4], main_box_vertices[5], main_box_vertices[6], main_box_vertices[7], main_box_vertices[4]],
            [main_box_vertices[0], main_box_vertices[4]], [main_box_vertices[1], main_box_vertices[5]],
            [main_box_vertices[2], main_box_vertices[6]], [main_box_vertices[3], main_box_vertices[7]]
        ]

        # Plot the edges of the main box
        for edge in main_box_edges:
            x_edge, y_edge, z_edge = zip(*edge)
            ax_main.plot(x_edge, y_edge, z_edge, color='b')

        # Set axis labels and title for the main box plot
        ax_main.set_xlabel('X')
        ax_main.set_ylabel('Y')
        ax_main.set_zlabel('Z')
        ax_main.set_title('Main Storage Box (Edges Only)')

        # Calculate the maximum side length of each item box
        max_item_side_length = sp.cbrt(max(volume for _, volume in items))

        # Calculate the number of item boxes in each dimension
        num_boxes_per_side = sp.ceiling(sp.cbrt(num_items))
        num_boxes = num_boxes_per_side ** 3

        # Plot the smaller item boxes (edges only)
        fig_items = plt.figure()
        ax_items = fig_items.add_subplot(111, projection='3d')

        # Plot the edges of each item box
        colors = plt.cm.rainbow(np.linspace(0, 1, num_items))
        idx = 0
        for i in range(num_boxes_per_side):
            for j in range(num_boxes_per_side):
                for k in range(num_boxes_per_side):
                    if idx < num_items:
                        x_item = i * max_item_side_length
                        y_item = j * max_item_side_length
                        z_item = k * max_item_side_length
                        weight, volume = items[idx]
                        item_side_length = sp.cbrt(volume)
                        # Define the vertices of the item box
                        item_box_vertices = np.array([[x_item, y_item, z_item],
                                                      [x_item + item_side_length, y_item, z_item],
                                                      [x_item + item_side_length, y_item + item_side_length, z_item],
                                                      [x_item, y_item + item_side_length, z_item],
                                                      [x_item, y_item, z_item + item_side_length],
                                                      [x_item + item_side_length, y_item, z_item + item_side_length],
                                                      [x_item + item_side_length, y_item + item_side_length, z_item + item_side_length],
                                                      [x_item, y_item + item_side_length, z_item + item_side_length]])

                        # Define the edges of the item box
                        item_box_edges = [
                            [item_box_vertices[0], item_box_vertices[1], item_box_vertices[2], item_box_vertices[3], item_box_vertices[0]],
                            [item_box_vertices[4], item_box_vertices[5], item_box_vertices[6], item_box_vertices[7], item_box_vertices[4]],
                            [item_box_vertices[0], item_box_vertices[4]], [item_box_vertices[1], item_box_vertices[5]],
                            [item_box_vertices[2], item_box_vertices[6]], [item_box_vertices[3], item_box_vertices[7]]
                        ]

                        # Plot the edges of the item box with transparency
                        for edge in item_box_edges:
                            x_edge, y_edge, z_edge = zip(*edge)
                            ax_items.plot(x_edge, y_edge, z_edge, color=colors[idx], alpha=0.5)
                        
                        idx += 1

        # Set axis labels and title for the item boxes plot
        ax_items.set_xlabel('X')
        ax_items.set_ylabel('Y')
        ax_items.set_zlabel('Z')
        ax_items.set_title('Item Boxes (Edges Only)')

        # Calculate the maximum dimension among all axes
        max_dim = max(x_val, y_val, z_val, max_item_side_length * num_boxes_per_side)

        # Set limits for each axis to the maximum value among all axes
        ax_main.set_xlim([0, float(max_dim)])
        ax_main.set_ylim([0, float(max_dim)])
        ax_main.set_zlim([0, float(max_dim)])

        ax_items.set_xlim([0, float(max_dim)])
        ax_items.set_ylim([0, float(max_dim)])
        ax_items.set_zlim([0, float(max_dim)])
        
plt.show()  # Display the plots
