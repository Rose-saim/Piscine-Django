from django.shortcuts import render

def generate_gradient(color, steps):
    """ Generate a list of shades for the given color. """
    shades = []
    for i in range(steps):
        # Calculate the shade by modifying the color intensity
        shade = (i * 255 // (steps - 1),) * 3  # RGB format
        if color == 'red':
            shade = (shade[0], 0, 0)  # Only red component
        elif color == 'green':
            shade = (0, shade[0], 0)  # Only green component
        elif color == 'blue':
            shade = (0, 0, shade[0])  # Only blue component
        elif color == 'black':
            shade = (0, 0, 0)  # Black
        shades.append(shade)
    return shades

from django.shortcuts import render

def ex03_view(request):
    # Generate color shades for red, green, blue, and black
    color_shades = {
        'red': [int(255 * (i / 50)) for i in range(51)],
        'green': [int(255 * (i / 50)) for i in range(51)],
        'blue': [int(255 * (i / 50)) for i in range(51)],
        'black': [0] * 51  # Black remains 0
    }
    
    # Prepare a list of indices for the loop in the template
    indices = list(range(51))

    return render(request, 'ex03/index.html', {
        'color_shades': color_shades,
        'indices': indices
    })
