use dec03::{load_input, part1, part2};


fn main() {
    let lines = load_input("./src/input.txt").expect("File doesn't exist");

    let test = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))";
    let test1 = part1(&test);
    println!("test 1 : {:?}", test1);

    let answer1 = part1(&lines);
    println!("answer 1 : {:?}", answer1);

    let test2 = part2(&test);
    println!("test 2 : {:?}", test2);

    let answer2 = part2(&lines);
    println!("answer 2 : {:?}", answer2);
}
