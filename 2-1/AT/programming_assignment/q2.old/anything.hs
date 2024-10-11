import Lsystem
import System.Random (StdGen, randomR, mkStdGen)
-- import System.Process (callCommand)

render' :: String -> System -> IO ()
render' = renderSystem (mkStdGen 42) (400,400)

-- n=4 f=12.5
-- X
-- X -> F − [[−X] + X] + F[+F X] − X, F + [[+X] − X] − F[−F X] + X[X]
-- F -> F[F]F, F[+]F, F[F F]F

dummy n = System {
    systemBasis = [x],
    systemRules = [
        StochasticRule [
            (0.5, DeterministicRule 
                ignoreContext 
                unconditional 
                (matchDummy "X")
                ( constantReplacement [ f, m, NodeBranch [[ NodeBranch [[m,x]], p, x ]], f, NodeBranch [[p,f,x]], m, x ] )
            ),
            (0.5, DeterministicRule 
                ignoreContext 
                unconditional 
                (matchDummy "X")
                ( constantReplacement [ f, p, NodeBranch [[ NodeBranch [[p,x]], m, x ]], f, NodeBranch [[m,f,x]], p, x ] )
            )
        ]
        , StochasticRule [
            (1/3, DeterministicRule
                ignoreContext
                unconditional
                ( matchDummy "F" )
                ( constantReplacement [ f, NodeBranch [[f]], f ] )
            ),
            (1/3, DeterministicRule
                ignoreContext
                unconditional
                ( matchDummy "F" )
                ( constantReplacement [ f, NodeBranch [[p]], f ] )
            ),
            (1/3, DeterministicRule
                ignoreContext
                unconditional
                ( matchDummy "F" )
                ( constantReplacement [ f, NodeBranch [[f,f]], f ] )
            )
        ]
    ],
    systemSteps = n
} where
    p = NodeRotate [] 12.5 0 0
    m = NodeRotate [] (-12.5) 0 0
    f = NodeDraw [] 1
    x = NodeDummy [] "X"

main :: IO ()
main = do
    render' "images/anything.svg" (dummy 5)
    -- mapM_ (\n -> render' ("random" ++ show n ++ ".png") (dummy n)) [1..4]
    -- callCommand "convert -delay 20 -loop 0 random*.png random.gif"
    -- callCommand "rm random*.png"