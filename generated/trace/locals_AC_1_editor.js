
if (allTraceData === undefined) {
    var allTraceData = {};
}
(function() { // IIFE to avoid variable collision
    let codelensID = "rs-locals_AC_1_editor";  //fallback
    let partnerCodelens = document.currentScript.parentElement.querySelector(".pytutorVisualizer");
    if (partnerCodelens) {
        codelensID = partnerCodelens.id;
    }
    allTraceData[codelensID] = {"code": "#include <iostream>\n\nvoid print_twice(char symbol);\n\nint main() {\n    char letter = 'b';\n    print_twice(letter);\n\n    return 0;\n}\n\nvoid print_twice(char symbol) {\n    std::cout << symbol << symbol << '\n';\n}\n", "trace": [{"exception_msg": "error: missing terminating ' character", "line": 13, "event": "uncaught_exception"}], "startingInstruction": 0};
})();