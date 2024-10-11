var anything_canvas = Array(5)
var anything_ctx = Array(5)
var anything = Array(5)
for (let i = 0; i < 5; i++) {
    anything_canvas[i] = document.getElementById(`anything${i+1}`);
    anything_ctx[i] = anything_canvas[i].getContext("2d");

    // translate to center of anything_canvas
    anything_ctx[i].translate(anything_canvas[i].width / 2, 3 * anything_canvas[i].height / 4);
    anything_ctx[i].scale(.5, .5);

    var n = 6;
    var a = 12.5;

    anything[i] = new LSystem({
        axiom: 'X',
        productions: {
            'X': () => (Math.random() < 1/2) ? 'F-[[-X]+X]+F[+FX]-X' : 'F+[[+X]-X]-F[-FX]+X', 
            'F': () => (Math.random() < 1/3) ? 'F[F]F' : ((Math.random() < 1/2) ? 'F[+]F' : 'F[FF]F')
        },
        finals: {
            '+': () => anything_ctx[i].rotate((Math.PI/180) * a),
            '-': () => anything_ctx[i].rotate((Math.PI/180) * -a),
            '[': () => anything_ctx[i].save(),
            ']': () => anything_ctx[i].restore(),
            'F': () => F(anything[i], anything_ctx[i])
        }
    });

    anything[i].iterate(n);
    anything[i].final();

    // var image = anything_canvas[i].toDataURL("image/png")
    // var link = document.createElement('a');
    // link.href = image;
    // link.download = `anything${i+1}.png`;
    // link.click();
}
