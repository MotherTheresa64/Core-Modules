let car = {
  name: "Lightning McQueen",
  model: "Race Car",
  year: 2006,
  start: function () {
    console.log(`Ka-chow! The ${this.year} ${this.name} is ready to roll!`);
  },
  drive: function () {
    console.log(`${this.name} is zooming at top speed! Vroom-vroom!`);
  },
  brake: function () {
    console.log(`${this.name} screeches to a halt!`);
  },
  honk: function () {
    console.log(`${this.name} honks: "Beep-beep! Clear the track!"`);
  }
};

car.start();
car.honk();
