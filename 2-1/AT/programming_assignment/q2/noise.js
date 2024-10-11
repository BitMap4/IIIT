var noise_canvas = document.getElementById('noise');
var noise_ctx = noise_canvas.getContext("2d");

// translate to center of noise_canvas
// mirror_ctx.translate(mirror_canvas.width / 2, mirror_canvas.height / 4);
noise_ctx.translate(280, 800);
noise_ctx.scale(.25, .25);

var n = 9;
var a = 90;

var noise = new LSystem({
    axiom: 'F+F',
    productions: {'F': 'F-F++F-F', 'F<F>-F': 'F-+F+F'},
    finals: {
        '+': () => noise_ctx.rotate((Math.PI/180) * a),
        '-': () => noise_ctx.rotate((Math.PI/180) * -a),
        '[': () => noise_ctx.save(),
        ']': () => noise_ctx.restore(),
        'F': () => F(noise, noise_ctx)
    }
});

noise.iterate(n);
noise.final();

// var image = noise_canvas.toDataURL("image/png")
// var link = document.createElement('a');
// link.href = image;
// link.download = `noise.png`;
// link.click();