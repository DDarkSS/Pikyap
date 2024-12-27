use std::env;
use std::io;

fn main() {
    let args: Vec<String> = env::args().collect();

    let (a, b, c) = if args.len() == 4 {
        // Парсинг коэффициентов из аргументов командной строки
        (
            args[1].parse::<f64>().unwrap_or_else(|_| {
                println!("Некорректный аргумент для A. Введите число:");
                get_number_from_user()
            }),
            args[2].parse::<f64>().unwrap_or_else(|_| {
                println!("Некорректный аргумент для B. Введите число:");
                get_number_from_user()
            }),
            args[3].parse::<f64>().unwrap_or_else(|_| {
                println!("Некорректный аргумент для C. Введите число:");
                get_number_from_user()
            }),
        )
    } else {
        // Ввод коэффициентов с клавиатуры
        println!("Введите коэффициент A:");
        let a = get_number_from_user();
        println!("Введите коэффициент B:");
        let b = get_number_from_user();
        println!("Введите коэффициент C:");
        let c = get_number_from_user();
        (a, b, c)
    };

    // Вычисление дискриминанта
    let discriminant = b * b - 4.0 * a * c;

    // Нахождение корней
    if discriminant > 0.0 {
        let x1 = (-b - discriminant.sqrt()) / (2.0 * a);
        let x2 = (-b + discriminant.sqrt()) / (2.0 * a);
        println!("Два различных действительных корня: x1 = {}, x2 = {}", x1, x2);
    } else if discriminant == 0.0 {
        let x = -b / (2.0 * a);
        println!("Один действительный корень: x = {}", x);
    } else {
        println!("Нет действительных корней");
    }
}

fn get_number_from_user() -> f64 {
    loop {
        let mut input = String::new();
        io::stdin()
            .read_line(&mut input)
            .expect("Ошибка при чтении строки");

        match input.trim().parse() {
            Ok(num) => return num,
            Err(_) => println!("Некорректный ввод. Введите число:"),
        }
    }
}
