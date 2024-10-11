var mirror_canvas = document.getElementById('mirrorball');
var mirror_ctx = mirror_canvas.getContext("2d");

// translate to center of canvas
mirror_ctx.translate(mirror_canvas.width / 2, 3 * mirror_canvas.height / 4);

var n = 12;
var a = 30;

var mirrorball = new LSystem({
    axiom: 'G',
    productions: {'G': 'X-G-X', 'X': 'G+Y+G', 'Y': '[+F]F[-F]'},
    finals: {
        '+': () => mirror_ctx.rotate((Math.PI/180) * a),
        '-': () => mirror_ctx.rotate((Math.PI/180) * -a),
        '[': () => mirror_ctx.save(),
        ']': () => mirror_ctx.restore(),
        'F': () => F(mirrorball, mirror_ctx),
        'G': () => G(mirrorball, mirror_ctx),
    }
});

mirrorball.iterate(n);
mirrorball.final();

// var image = mirror_canvas.toDataURL("image/png")
// var link = document.createElement('a');
// link.href = image;
// link.download = `mirrorball.png`;
// link.click();