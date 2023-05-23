// const input = require('fs').readFileSync('/dev/stdin', 'utf8');
// const lines = input.split('\n');

function main() {
    const n = Number(lines[0])

    for (let i = n; i < n + 12; i++) {
        if (i % 2 !== 0) {
            console.log(i)
        }
    }
}

main()

