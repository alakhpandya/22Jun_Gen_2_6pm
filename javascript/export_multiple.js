const capitalizeString = (str) => {
    return str.charAt([0]).toUpperCase() + str.slice(1, str.length);
};

const capitalizeLastCharacter = (str) => {
    return str.slice(0, str.length-1) + str.charAt([str.length - 1]).toUpperCase();
}

export const pi = 3.1415;
export const e = 2.73;
export {capitalizeString, capitalizeLastCharacter}
