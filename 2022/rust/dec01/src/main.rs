use dec01::{load_input, part1, part2};


fn main() {
    let lines = load_input("./src/input.txt").expect("File doesn't exist");
    let answer1 = part1(Ok(lines));
    println!("answer 1 : {:?}", answer1);

    let lines2 = load_input("./src/input.txt").expect("File doesn't exist");
    let answer2 = part2(Ok(lines2));
    println!("answer 2 : {:?}", answer2);

}
