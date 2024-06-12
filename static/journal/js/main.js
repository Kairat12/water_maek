let factAttributes = document.querySelectorAll(".fact_attributes");
if (factAttributes){
    numberAlert();
}
function numberAlert() {
    let factNormal = document.querySelectorAll(".fact_normal");
    factAttributes.forEach((el) => {
        let factValues = el.querySelectorAll(".attribute");
        let factNormal = el.previousElementSibling;
        let normalValues = factNormal.querySelectorAll(".normal_value");
        factValues.forEach((el, index) => {
            let factValueText = el.querySelector(".editable") ? el.querySelector(".editable").value : NaN;
            let factValue = parseFloat(factValueText)
            // Используем индекс итерации для обращения к соответствующему элементу в normalValues
            let normalValueElement = normalValues[index];
            if (normalValueElement) {
                let normalValue = normalValueElement.dataset.value;
                if (normalValue.includes('-')) {
                    let values = normalValue.split('-');
                    let number1 = parseFloat(values[0]);
                    let number2 = parseFloat(values[1]);
                    console.log("normalValue", number1, number2);
                    if (number1 > number2) {
                        let temp = number1;
                        number1 = number2;
                        number2 = temp;
                    }
                    console.log("normalValue", number1, number2);
                    if ((!isNaN(number1) && !isNaN(number2)) && ((number1 > factValue) || (factValue > number2)) && normalValue !== "not") {
                        el.classList.add("bg-danger");
                        el.classList.add("text-white");
                    }
                } else if (normalValue.includes('>') && factValue < parseFloat(normalValue.substring(1))) {
                    el.classList.add("bg-danger");
                    el.classList.add("text-white");
                } else if (!isNaN(parseFloat(normalValue)) && factValue > parseFloat(normalValue) && normalValue !== "not") {
                    el.classList.add("bg-danger");
                    el.classList.add("text-white");
                }
            } else {
                console.error("Normal value element not found at index", index);
            }
        });
    })
}