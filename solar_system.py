import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1600, 1000))
clock = pygame.time.Clock()

sun_color = (255, 255, 0)

# Planet data
planets = [
    {"color": (100, 100, 100), "radius": 13, "distance": 77, "angle": 0, "rotation_speed": 1},    # Mercury
    {"color": (150, 100, 0), "radius": 15, "distance": 122, "angle": 0, "rotation_speed": 0.9},   # Venus
    {"color": (0, 70, 150), "radius": 30, "distance": 200, "angle": 0, "rotation_speed": 0.6},    # Earth
    {"color": (200, 70, 0), "radius": 40, "distance": 314, "angle": 0, "rotation_speed": 0.4},    # Mars
    {"color": (176, 127, 53), "radius": 60, "distance": 470, "angle": 0, "rotation_speed": 0.3},  # Jupíter
    {"color": (156, 143,114), "radius": 50, "distance": 660, "angle": 0, "rotation_speed": 0.3},  # Saturn
    {"color": (120, 120, 200), "radius": 30, "distance": 850, "angle": 0, "rotation_speed": 0.2}, # Uranus
    {"color": (70, 70, 200), "radius": 40, "distance": 1000, "angle": 0, "rotation_speed": 0.1},  # Neptune
]

# Planet trajectories
trajectories = [
    {"color": (100, 100, 100), "distance": 77},  # Mercury
    {"color": (150, 100, 0), "distance": 122},   # Venus
    {"color": (0, 70, 150), "distance": 200},    # Earth
    {"color": (200, 70, 0), "distance": 314},    # Mars
    {"color": (176, 127, 53), "distance": 470},  # Jupíter
    {"color": (156, 143,114), "distance": 660},  # Saturn
    {"color": (120, 120, 200), "distance": 850}, # Uranus
    {"color": (70, 70, 200), "distance": 1000}   # Neptune
]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, sun_color, (500, 400), 40)
    
    # Draw planets
    for planet in planets:
        planet_x = 500 + planet["distance"] * pygame.math.Vector2(1, 0).rotate(planet["angle"]).x
        planet_y = 400 + planet["distance"] * pygame.math.Vector2(1, 0).rotate(planet["angle"]).y
        pygame.draw.circle(screen, planet["color"], (int(planet_x), int(planet_y)), planet["radius"])
        planet["angle"] += planet["rotation_speed"]

    # Draw trajectories
    for i in trajectories:
        for angle in range(0, 360, 10):
            traj_x = 500 + i["distance"] * pygame.math.Vector2(1,0).rotate(angle).x
            traj_y = 400 + i["distance"] * pygame.math.Vector2(1,0).rotate(angle).y
            pygame.draw.circle(screen, i["color"], (int(traj_x), int(traj_y)), 2)

    pygame.display.flip()
    clock.tick(60)
