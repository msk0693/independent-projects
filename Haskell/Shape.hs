type Dim1 = Double
type Dim2 = Double

data Shape = Circle Dim1
		   | Rectangle Dim1 Dim2
		   | Triangle Dim1 Dim2
		   deriving (Show)
area Circle  = pi * Dim1 * Dim1


