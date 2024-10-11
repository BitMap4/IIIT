# import Pkg; Pkg.add("StringDistances")

using StringDistances

function main()
    ref = join.(split.(eachline(ARGS[1])))
    hyp = join.(split.(eachline(ARGS[2])))

    @assert length(ref) == length(hyp)

    # Accuracy
    correct = sum(ref .== hyp)
    n = length(ref)
    println("Accuracy: $correct / $n   $(correct / n)")

    # Character edit distance
    ced = 0
    for (r, h) in zip(ref, hyp)
        ced += Levenshtein()(r, h)
    end
    println("Character edit distance ", ced / length(ref))

    # Errors
    for (r, h) in zip(ref, hyp)
        if r != h
            println(r, " -> ", h)
        end
    end
end

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end