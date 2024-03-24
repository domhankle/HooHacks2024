export function paginateData(data: any[], pageIndex: number, pageSize: number): any[] {
    const start = pageIndex * pageSize;
    const toReturn = [];
    for (let i = 0; i < pageSize; ++i) {
        if (start + i === data.length) {
            break;
        }
        toReturn.push(data[start + i]);
    }

    return toReturn;
}