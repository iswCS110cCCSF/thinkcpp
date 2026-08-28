
if (allTraceData === undefined) {
    var allTraceData = {};
}
(function() { // IIFE to avoid variable collision
    let codelensID = "rs-multiple_functions_AC_1_editor";  //fallback
    let partnerCodelens = document.currentScript.parentElement.querySelector(".pytutorVisualizer");
    if (partnerCodelens) {
        codelensID = partnerCodelens.id;
    }
    allTraceData[codelensID] = {"code": "#include <iostream>\n\n// Function declarations\nvoid print_total(int x);\nint multiply_two(int x);\nint add_two(int x);\n\nint main() {\n    int num = 3;\n\n    int new_num = multiply_two(num);\n    int newer_num = add_two(new_num);\n\n    print_total(newer_num);\n\n    return 0;\n}\n\n// Function definitions\nvoid print_total(int x) {\n    std::cout << x << '\n';\n}\n\nint multiply_two(int x) {\n    int total = x * 2;\n    print_total(total);\n    return total;\n}\n\nint add_two(int x) {\n    int total = x + 2;\n    return total;\n}\n", "trace": [{"exception_msg": "error: missing terminating ' character", "line": 21, "event": "uncaught_exception"}], "startingInstruction": 0};
})();