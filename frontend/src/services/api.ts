import axios from 'axios';

const baseURL = 'http://localhost:8000/api';

export const getLegislatorsBills = async () => {
    const url = `${baseURL}/legislator/analytics/`;
    return await axios.get(url);
}

export const getBillsDetails = async () => {
    const url = `${baseURL}/bill/analytics/`;
    return await axios.get(url);
}