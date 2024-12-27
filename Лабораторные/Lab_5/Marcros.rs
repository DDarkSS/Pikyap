#[derive(Debug)] 
struct Point {
    x: i32,
    y: i32,
}

fn main() {
    let point = Point { x: 10, y: 20 };
    println!("{:?}", point); 
}