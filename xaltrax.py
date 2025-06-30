import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Setup figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-20, 20])
ax.set_ylim([-20, 20])
ax.set_zlim([0, 10])
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("6-DOF Robotic Arm: Pick-and-Place with Gripper")

# Arm settings
num_joints = 6
link_lengths = [3] * num_joints
line, = ax.plot([], [], [], 'ro-', lw=3)
gripper_lines = [ax.plot([], [], [], 'g-')[0], ax.plot([], [], [], 'g-')[0]]

# Pick and place points
point_a = np.array([10, 0, 0])
point_b = np.array([0, 10, 0])
ax.scatter(*point_a, c='green', s=40, label='Pick Point')
ax.scatter(*point_b, c='blue', s=40, label='Place Point')
ax.legend()

# Animate angles (approximate sine wave motion)
def generate_angles(frame):
    progress = frame / 150
    if frame < 50:  # move to pick
        angles = [30 * np.sin(progress * np.pi) for _ in range(num_joints)]
    elif frame < 75:  # grip
        angles = [45 for _ in range(num_joints)]
    elif frame < 125:  # move to place
        shift = (frame - 75) / 50
        angles = [45 - 20 * shift for _ in range(num_joints)]
    else:  # release
        angles = [25 for _ in range(num_joints)]
    return angles

# Forward Kinematics
def forward_kinematics(angles, lengths):
    x, y, z = 0, 0, 0
    total_angle = 0
    points = [(x, y, z)]

    for i in range(len(angles)):
        total_angle += np.radians(angles[i])
        dx = lengths[i] * np.cos(total_angle)
        dy = lengths[i] * np.sin(total_angle)
        x += dx
        y += dy
        points.append((x, y, z))  # planar arm
    return points

# Gripper logic
def update_gripper(points, frame):
    end = np.array(points[-1])
    last_vec = np.array(points[-1]) - np.array(points[-2])
    last_vec = last_vec / np.linalg.norm(last_vec)
    # perpendicular to last link in XY plane
    perp = np.array([-last_vec[1], last_vec[0], 0])

    spread = 1.0 if (50 <= frame < 75 or frame >= 125) else 0.2  # open except while carrying
    g1 = end + perp * spread
    g2 = end - perp * spread

    for gripper, pt in zip(gripper_lines, [g1, g2]):
        gripper.set_data([end[0], pt[0]], [end[1], pt[1]])
        gripper.set_3d_properties([end[2], pt[2]])

# Animation update
def update(frame):
    angles = generate_angles(frame)
    points = forward_kinematics(angles, link_lengths)
    xs, ys, zs = zip(*points)
    line.set_data(xs, ys)
    line.set_3d_properties(zs)
    update_gripper(points, frame)
    return line, *gripper_lines

ani = FuncAnimation(fig, update, frames=160, interval=100, blit=False)
plt.show()

