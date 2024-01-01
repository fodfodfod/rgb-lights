use std::cmp::Ordering;
use std::thread;
use std::time;
use rppal::gpio::Gpio;

static RED_PORT: u8 = 4;
static GREEN_PORT: u8 = 5;
static BLUE_PORT: u8 = 6;
static TIME_CONSTANT: f64 = 1.0;


fn main() {
    println!("Hello, world!");

    let mut values: Color = Color::new();
    let mut red_pin = Gpio::new().unwrap().get(RED_PORT).unwrap().into_output();
    let mut green_pin = Gpio::new().unwrap().get(GREEN_PORT).unwrap().into_output();
    let mut blue_pin = Gpio::new().unwrap().get(BLUE_PORT).unwrap().into_output();
    println!("hi again");
    //red_pin.set_high();
    //green_pin.set_high();
    //blue_pin.set_high();
    loop{
        values.rainbow_cycle();
        controller(&values, &mut red_pin, &mut green_pin, &mut blue_pin);
        controller(&values, &mut red_pin, &mut green_pin, &mut blue_pin);
        controller(&values, &mut red_pin, &mut green_pin, &mut blue_pin);
        controller(&values, &mut red_pin, &mut green_pin, &mut blue_pin);
        controller(&values, &mut red_pin, &mut green_pin, &mut blue_pin);
        controller(&values, &mut red_pin, &mut green_pin, &mut blue_pin);
        controller(&values, &mut red_pin, &mut green_pin, &mut blue_pin);
        controller(&values, &mut red_pin, &mut green_pin, &mut blue_pin);
        controller(&values, &mut red_pin, &mut green_pin, &mut blue_pin);
        controller(&values, &mut red_pin, &mut green_pin, &mut blue_pin);
        controller(&values, &mut red_pin, &mut green_pin, &mut blue_pin);
        controller(&values, &mut red_pin, &mut green_pin, &mut blue_pin);
        controller(&values, &mut red_pin, &mut green_pin, &mut blue_pin);
        controller(&values, &mut red_pin, &mut green_pin, &mut blue_pin);
    }
}

fn controller(color: &Color, red_pin: &mut rppal::gpio::OutputPin, green_pin: &mut rppal::gpio::OutputPin, blue_pin: &mut rppal::gpio::OutputPin){

    red_pin.set_high();
    green_pin.set_high();
    blue_pin.set_high();
    let mut list = color.convert_to_list(); 
    list.sort();
    //list.reverse();
    

    let wait_time = list.get(0).unwrap().intensity;
    thread::sleep(time::Duration::from_micros((wait_time as f64*TIME_CONSTANT)as u64)); 
    match channel_to_enum(list[0].port){
        RGB::RED => red_pin.set_low(),
        RGB::GREEN => green_pin.set_low(),
        RGB::BLUE => blue_pin.set_low(),
    }; 
    
    let wait_time = list.get(1).unwrap().intensity - list.get(0).unwrap().intensity;
    thread::sleep(time::Duration::from_micros((wait_time as f64*TIME_CONSTANT)as u64)); 
    match channel_to_enum(list[1].port){
        RGB::RED => red_pin.set_low(),
        RGB::GREEN => green_pin.set_low(),
        RGB::BLUE => blue_pin.set_low(),
    }; 
    
    let wait_time = list.get(2).unwrap().intensity - list.get(1).unwrap().intensity - list.get(0).unwrap().intensity;
    thread::sleep(time::Duration::from_micros((wait_time as f64*TIME_CONSTANT)as u64)); 
    
    match channel_to_enum(list[2].port){
        RGB::RED => red_pin.set_low(),
        RGB::GREEN => green_pin.set_low(),
        RGB::BLUE => blue_pin.set_low(),
    }; 
    let wait_time = 255 - list.get(2).unwrap().intensity - list.get(1).unwrap().intensity - list.get(0).unwrap().intensity;
    thread::sleep(time::Duration::from_micros((wait_time as f64*TIME_CONSTANT)as u64)); 
    //
}

fn channel_to_enum(channel: u8) -> RGB{
    if channel == RED_PORT{
        return RGB::RED;
    }
    if channel == GREEN_PORT{
        return RGB::GREEN;
    }
    return RGB::BLUE;
}

#[derive(Copy)]
#[derive(Clone)]
struct LED{
    intensity: u8,
    port: u8
}

impl Ord for LED{
    fn cmp(&self, other: &Self) -> Ordering{
        (self.intensity).cmp(&other.intensity)
    }
}
impl PartialOrd for LED{
    fn partial_cmp(&self, other: &Self) -> Option<Ordering>{
        Some(self.cmp(other))
    }
}
impl PartialEq for LED{
    fn eq(&self, other: &Self) -> bool {
        self.intensity == other.intensity
    }
}
impl Eq for LED { }

enum RGB {
    RED,
    GREEN,
    BLUE
}

struct Color{
    red: LED,
    green: LED,
    blue: LED,
}

impl Color{
    fn new() -> Self {
        Color { red: LED{ intensity: 255, port: RED_PORT}, green: LED{ intensity: 0, port: GREEN_PORT}, blue: LED { intensity: 0, port: BLUE_PORT}}
    }
    pub fn rainbow_cycle(&mut self) {
        if self.red.intensity == 255 && self.green.intensity < 255 && self.blue.intensity == 0 {
            self.green.intensity += 1;
        }
        if self.red.intensity > 0 && self.green.intensity == 255 && self.blue.intensity == 0 {
            self.red.intensity -= 1;
        }
        if self.red.intensity == 0 && self.green.intensity == 255 && self.blue.intensity < 255 {
            self.blue.intensity += 1;
        }
        if self.red.intensity == 0 && self.green.intensity > 0 && self.blue.intensity == 255 {
            self.green.intensity -= 1;
        }
        if self.red.intensity < 255 && self.green.intensity == 0 && self.blue.intensity == 255 {
            self.red.intensity += 1;
        }
        if self.red.intensity == 255 && self.green.intensity == 0 && self.blue.intensity > 0 {
            self.blue.intensity -= 1;
        }
    }
    pub fn convert_to_list(&self) -> [LED; 3]{
        let list = [self.red, self.green, self.blue];
        list
    }
}
