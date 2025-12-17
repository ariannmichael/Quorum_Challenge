import axios from 'axios';
import { downloadCSV } from '../utils/downloadCSV';


const baseURL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';

export const getLegislatorsBills = async () => {
    const url = `${baseURL}/legislators/analytics/`;
    return await axios.get(url);
}

export const getBillsDetails = async () => {
    const url = `${baseURL}/bills/analytics/`;
    return await axios.get(url);
}

export const uploadBills = async (file: any) => {
    const url = `${baseURL}/bills/import/`;
    const formData = new FormData();
    formData.append("file", file);

    return await axios.post(url, formData, {
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    });
}

export const uploadLegislators = async (file: any) => {
    const url = `${baseURL}/legislators/import/`;
    const formData = new FormData();
    formData.append("file", file);

    return await axios.post(url, formData, {
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    });
}

export const uploadVotes = async (file: any) => {
    const url = `${baseURL}/votes/import/`;
    const formData = new FormData();
    formData.append("file", file);

    return await axios.post(url, formData, {
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    });
}

export const uploadVoteResults = async (file: any) => {
    const url = `${baseURL}/vote-results/import/`;
    const formData = new FormData();
    formData.append("file", file);

    return await axios.post(url, formData, {
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    });
}

export const downloadLegislators = async (filename: string) => {
    const url = `${baseURL}/legislators/export/`;
    downloadCSV(url, filename);
}

export const downloadBills = async (filename: string) => {
    const url = `${baseURL}/bills/export/`;
    downloadCSV(url, filename);
}