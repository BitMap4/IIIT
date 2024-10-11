import Lsystem
import System.Random (mkStdGen)
-- import System.Process (callCommand)

render' :: String -> System -> IO ()
render' = renderSystem (mkStdGen 42) (400,400)

-- n=9 f=90
-- F+F
-- F -> F-F++F-F
-- F<F>-F -> F-+F+F

dummy n = System {
    systemBasis = [f, p, f],
    systemRules = [
        DeterministicRule {
            ruleContext = contextMatch [] ,
            ruleCondition = unconditional,
            ruleMatch = matchDummy "X",
            ruleReplacement = constantReplacement [
                f, NodeBranch [[m,x]], x, NodeBranch [[p,x]], NodeBranch [[p,x]], f, m, NodeBranch [[m,x]], p, x, NodeBranch [[m,x]]
            ]
        },
        DeterministicRule {
            ruleContext = ignoreContext,
            ruleCondition = unconditional,
            ruleMatch = matchDummy "F",
            ruleReplacement = constantReplacement [f, f]
        }
    ],
    systemSteps = n
} where
    p = NodeRotate [] 15 0 0
    m = NodeRotate [] (-15) 0 0
    f = NodeDraw [] 1

main :: IO ()
main = do
    render' "images/tree.svg" (dummy 4)
    -- mapM_ (\n -> render' ("tree" ++ show n ++ ".png") (dummy n)) [1..4]
    -- callCommand "convert -delay 20 -loop 0 tree*.png tree.gif"
    -- callCommand "rm tree*.png"