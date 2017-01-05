import java.io._

class Point2D(val xc: Int, val yc: Int){
	var x: Int = xc
	var y: Int = yc

	def move(dx: Int, dy: Int){
		x = x + dx
		y = y + dy

		println ("Point x location : " + x);
		println ("Point y location : " + y);

	}
}
class Location(override val xc: Int, override val yc: Int val zc: Int) extends Point2D(xc,yc){
	var z: Int = zc

	def move(dx: Int, dy: Int, dz: Int){
		x = x + dx
		y = y + dy
		z = z + dz
		println ("Point x location : " + x);
		println ("Point y location : " + y);
		println ("Point z location : " + z);

	}
}
object PointDemo {
	def main(args: Array[String]){
		val pt2d = new Point2D(10,30);
		val pt3d = new Point3D(10,30,50);
		pt2d.move(10,10);
		pt3d.move(10,10,10);
	}
}