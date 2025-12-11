import tkinter as tk
import random
global spawn_particles
# Setup window
root = tk.Tk()
root.title("Particle Effects")
canvas = tk.Canvas(root, width=1500, height=1500, bg="black")
canvas.pack()

particles = []  # Store all particles

def create_particle():
    # Random starting position in the middle
    x = 670
    y = 400

    # Random size and color
    size = random.randint(4, 20)
    color = random.choice(["yellow", "orange", "white", "cyan", "magenta"])

    # Create the particle (a small circle)
    particle_id = canvas.create_oval(x, y, x + size, y + size, fill=color, outline="")

    # Particle dictionary
    particle = {
        "id": particle_id,
        "dx": random.uniform(-10, 10),   # horizontal movement
        "dy": random.uniform(-10, 10), # upward/wind movement
        "life": random.randint(40, 100) # frames before disappearing
    }

    particles.append(particle)

def stop_spawning():
    spawn_particles = False
    print("Particle spawning stopped!")

def update_particles():
    # Update and remove dead particles
    for p in particles[:]:
        canvas.move(p["id"], p["dx"], p["dy"])
        p["dy"] += 0.05
        p["life"] -= 1

        if p["life"] <= 0:
            canvas.delete(p["id"])
            particles.remove(p)

    # Only create particles if spawning is still allowed
    if spawn_particles:
        for _ in range(3):
            create_particle()

    root.after(30, update_particles)



# Stop creating particles after 5 seconds
root.after(5000, stop_spawning)

update_particles()
root.mainloop()