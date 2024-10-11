var tree_canvas = document.getElementById('tree');
var tree_ctx = tree_canvas.getContext("2d");

// translate to center of tree_canvas
tree_ctx.translate(tree_canvas.width / 2, 3 * tree_canvas.height / 4);
tree_ctx.scale(.7, .7);

var n = 4;
var r = 9;
var a = r%30 - 15 + 10*(-1)**(15 - r%30);
// var a = 15;

var tree = new LSystem({
    axiom: 'X',
    productions: {'X': 'F[-X]X[+X][+X]F-[-X]+X[-X]', 'F': 'FF'},
    finals: {
        '+': () => tree_ctx.rotate((Math.PI/180) * a),
        '-': () => tree_ctx.rotate((Math.PI/180) * -a),
        '[': () => tree_ctx.save(),
        ']': () => tree_ctx.restore(),
        'F': () => F(tree, tree_ctx)
    }
});

tree.iterate(n);
tree.final();

// var image = tree_canvas.toDataURL("image/png")
// var link = document.createElement('a');
// link.href = image;
// link.download = `tree.png`;
// link.click();