
if (allTraceData === undefined) {
    var allTraceData = {};
}
(function() { // IIFE to avoid variable collision
    let codelensID = "rs-multiple_functions_AC_1_editor";  //fallback
    let partnerCodelens = document.currentScript.parentElement.querySelector(".pytutorVisualizer");
    if (partnerCodelens) {
        codelensID = partnerCodelens.id;
    }
    allTraceData[codelensID] = {"code": "#include <iostream>\n\nvoid print_total(int x) {\n    std::cout << x << '\n';\n}\n\nint multiply_two(int x) {\n    int total = x * 2;\n    print_total(total);\n    return total;\n}\n\nint add_two(int x) {\n    int total = x + 2;\n    return total;\n}\n\nint main() {\n    int num = 3;\n    int newNum = multiply_two(num);\n    int newerNum = add_two(newNum);\n    print_total(newerNum);\n    return 0;\n}\n", "trace": [{"exception_msg": "error: missing terminating ' character", "line": 4, "event": "uncaught_exception"}], "startingInstruction": 0};
})();