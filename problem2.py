from geomdl import BSpline
from geomdl import utilities
from geomdl.visualization import VisMPL
from geomdl import operations
from geomdl import multi

# Curve 1
# Create a B-Spline curve instance (Bezier Curve)
curve1 = BSpline.Curve()

# Set up the Bezier curve
curve1.degree = 3
curve1.ctrlpts = [[-2.5,9.2],[-3,9.7],[-5.5,10.5],[-6,10]]

# Auto-generate knot vector
curve1.knotvector = utilities.generate_knot_vector(curve1.degree, len(curve1.ctrlpts))

# Curve 2
# Create a B-Spline curve instance (Bezier Curve)
curve2 = BSpline.Curve()

# Set up the Bezier curve
curve2.degree = 3
curve2.ctrlpts = [[-6,10],[-6.5,9.5],[-6.9,6.5],[-6.5,6]]

# Auto-generate knot vector
curve2.knotvector = utilities.generate_knot_vector(curve2.degree, len(curve2.ctrlpts))

# Curve 3
# Create a B-Spline curve instance (Bezier Curve)
curve3 = BSpline.Curve()

# Set up the Bezier curve
curve3.degree = 3
curve3.ctrlpts = [[-6.5,6],[-12.5,-6.1],[13.5,-6.6],[6.3,6.5]]

# Auto-generate knot vector
curve3.knotvector = utilities.generate_knot_vector(curve3.degree, len(curve3.ctrlpts))

# Curve 4
# Create a B-Spline curve instance (Bezier Curve)
curve4 = BSpline.Curve()

# Set up the Bezier curve
curve4.degree = 3
curve4.ctrlpts = [[6.3,6.5],[6.8,7],[7.2,9.7],[6.5,10.5]]

# Auto-generate knot vector
curve4.knotvector = utilities.generate_knot_vector(curve4.degree, len(curve4.ctrlpts))


# Curve 5
# Create a B-Spline curve instance (Bezier Curve)
curve5 = BSpline.Curve()

# Set up the Bezier curve
curve5.degree = 3
curve5.ctrlpts = [[6.5,10.5],[6,11],[3,9.7],[2.5,9.2]]

# Auto-generate knot vector
curve5.knotvector = utilities.generate_knot_vector(curve5.degree, len(curve5.ctrlpts))


# Curve 6
# Create a B-Spline curve instance (Bezier Curve)
curve6 = BSpline.Curve()

# Set up the Bezier curve
curve6.degree = 3
curve6.ctrlpts = [[2.5,9.2],[0.5,9.6],[-0.5,9.6],[-2.5,9.2]]

# Auto-generate knot vector
curve6.knotvector = utilities.generate_knot_vector(curve6.degree, len(curve6.ctrlpts))



# Create a curve container
mcrv = multi.CurveContainer(curve1,curve2,curve3,curve4,curve5,curve6)

# Rotate curve container
mcrv = operations.rotate(mcrv,9.5)

# Set the visualization component of the curve container
mcrv.vis = VisMPL.VisCurve2D(ctrlpts=True)

# Plot the curves in the curve container
mcrv.render()
