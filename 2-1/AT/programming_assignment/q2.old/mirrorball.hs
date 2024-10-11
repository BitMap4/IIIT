import Lsystem
import System.Random (mkStdGen)
-- import Lsystem.Grammar (Node(NodeDummy))
import System.Process (callCommand)
import Lsystem.Grammar (Node(NodeWidth))

render' :: String -> System -> IO ()
render' = renderSystem (mkStdGen 42) (400,400)

-- n=9 f=30
-- G
-- G -> X-G-X
-- X -> G+Y+G
-- Y -> [+F]F[-F]

dummy n = System {
    systemBasis = [g],
    systemRules = [
        DeterministicRule {
            ruleContext = ignoreContext,
            ruleCondition = unconditional,
            ruleMatch = matchDraw 2,
            ruleReplacement = constantReplacement [ x, m, g, m, x ]
        },
        DeterministicRule {
            ruleContext = ignoreContext,
            ruleCondition = unconditional,
            ruleMatch = matchDummy "X",
            ruleReplacement = constantReplacement [ g, p, y, p, g ]
        },
        DeterministicRule {
            ruleContext = ignoreContext,
            ruleCondition = unconditional,
            ruleMatch = matchDummy "Y",
            ruleReplacement = constantReplacement [ NodeBranch [[p,f]], f, NodeBranch [[m,f]] ]
        }
    ],
    systemSteps = n
} where
    p = NodeRotate [] 30 0 0
    m = NodeRotate [] (-30) 0 0
    f = NodeDraw [] 1
    g = NodeDraw [] 2
    x = NodeDummy [] "X"
    y = NodeDummy [] "Y"

main :: IO ()
main = do
    render' "images/mirrorball.svg" (dummy 9)
    -- mapM_ (\n -> render' ("images/mirrorball" ++ show n ++ ".svg") (dummy n)) [1..10]