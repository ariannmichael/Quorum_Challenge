import { describe, it, expect, vi, beforeEach } from 'vitest'
import axios from 'axios'
import * as api from './api'

// Mock axios
vi.mock('axios', () => ({
  default: {
    get: vi.fn(),
    post: vi.fn(),
  }
}))

const mockedAxios = axios as any

describe('API Service', () => {
  beforeEach(() => {
    vi.clearAllMocks()
  })

  describe('getLegislatorsBills', () => {
    it('calls the correct endpoint', async () => {
      const mockData = { data: [] }
      mockedAxios.get.mockResolvedValue(mockData)

      await api.getLegislatorsBills()

      expect(mockedAxios.get).toHaveBeenCalledWith(
        expect.stringContaining('/legislators/analytics/')
      )
    })

    it('returns the response data', async () => {
      const mockData = { data: [{ legislator: { id: 1, name: 'Test' } }] }
      mockedAxios.get.mockResolvedValue(mockData)

      const result = await api.getLegislatorsBills()

      expect(result).toEqual(mockData)
    })
  })

  describe('getBillsDetails', () => {
    it('calls the correct endpoint', async () => {
      const mockData = { data: [] }
      mockedAxios.get.mockResolvedValue(mockData)

      await api.getBillsDetails()

      expect(mockedAxios.get).toHaveBeenCalledWith(
        expect.stringContaining('/bills/analytics/')
      )
    })
  })

  describe('uploadBills', () => {
    it('calls the correct endpoint with FormData', async () => {
      const mockFile = new File(['test'], 'test.csv', { type: 'text/csv' })
      const mockResponse = { data: { message: 'Success' } }
      mockedAxios.post.mockResolvedValue(mockResponse)

      await api.uploadBills(mockFile)

      expect(mockedAxios.post).toHaveBeenCalledWith(
        expect.stringContaining('/bills/import/'),
        expect.any(FormData),
        expect.objectContaining({
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
      )
    })
  })

  describe('uploadLegislators', () => {
    it('calls the correct endpoint with FormData', async () => {
      const mockFile = new File(['test'], 'test.csv', { type: 'text/csv' })
      const mockResponse = { data: { message: 'Success' } }
      mockedAxios.post.mockResolvedValue(mockResponse)

      await api.uploadLegislators(mockFile)

      expect(mockedAxios.post).toHaveBeenCalledWith(
        expect.stringContaining('/legislators/import/'),
        expect.any(FormData),
        expect.objectContaining({
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
      )
    })
  })
})

