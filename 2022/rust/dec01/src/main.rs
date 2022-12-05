use dec01::{load_input, part1};


fn main() {
    let lines = load_input("./src/input.txt").expect("File doesn't exist");
    let answer = part1(Ok(lines));
    println!("{:?}", answer);
}
