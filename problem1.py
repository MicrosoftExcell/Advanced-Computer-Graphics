from geomdl import BSpline
from geomdl import operations
from geomdl.visualization import VisMPL

# Create a B-Spline curve
curve = BSpline.Curve()

# Set degree
curve.degree = 2

# Set control points
curve.ctrlpts = [[-6.5,6],[-9.8,-3.2],[10.4,-3],[6.5,6.6],[8.3,13.2],[2.5,9.2],[0,9.9],[-2.5,9.2],[-7.8,12.4],[-6.5,6]]

# Set knot vector
curve.knotvector = [0.0, 0.0, 0.0, 0.13, 0.25, 0.25, 0.5, 0.5, 0.75, 0.75, 1.0, 1.0, 1.0]

# Set evaluation delta
curve.delta = 0.005

# Rotate curve
curve = operations.rotate(curve,9.5)

# Scale curve
curve = operations.scale(curve,2)

# Plot the control point polygon and the evaluated curve
curve.vis = VisMPL.VisCurve2D(ctrlpts=False)
curve.render()
