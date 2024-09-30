struct User {
    email: String,
    password: String,
}

impl User {
    fn new(email: &str, password: &str) -> User {
        User {
            email: email.to_string(),
            password: password.to_string(),
        }
    }
}

fn main() {
    let user = User::new("example@example.com", "password123");
    println!("Email: {}", user.email);
    println!("Password: {}", user.password);
}