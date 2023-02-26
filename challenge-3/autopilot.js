function controlCar(scanArray) {
    if (scanArray[7] > 12 && scanArray[8] > 12 && scanArray[9] > 12) {
        return 0
    } else {
        if (scanArray[4] + scanArray[5] + scanArray[6] > scanArray[10] + scanArray[11] + scanArray[12] && scanArray[6] !== 0) {
            return -1
        } else if (scanArray[10] !== 0) {
            return 1
        }
    }
}