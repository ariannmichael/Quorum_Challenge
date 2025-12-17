import { describe, it, expect, vi, beforeEach } from 'vitest'
import { render, screen, waitFor } from '@testing-library/react'
import { BrowserRouter } from 'react-router-dom'
import Legislators from './Legislators'
import * as api from '../../../services/api'

// Mock the API module
vi.mock('../../../services/api', () => ({
  getLegislatorsBills: vi.fn(),
  downloadLegislators: vi.fn()
}))

describe('Legislators', () => {
  const mockLegislatorsData = [
    {
      legislator: {
        id: 1,
        name: 'John Doe'
      },
      supported_bills: 10,
      opposed_bills: 5
    },
    {
      legislator: {
        id: 2,
        name: 'Jane Smith'
      },
      supported_bills: 20,
      opposed_bills: 15
    }
  ]

  beforeEach(() => {
    vi.clearAllMocks()
  })

  it('renders legislators header and download button', () => {
    vi.mocked(api.getLegislatorsBills).mockResolvedValue({ data: mockLegislatorsData } as any)
    
    render(
      <BrowserRouter>
        <Legislators />
      </BrowserRouter>
    )

    expect(screen.getByText('Legislators')).toBeInTheDocument()
    expect(screen.getByText('Download CSV')).toBeInTheDocument()
  })

  it('displays legislators when data is loaded', async () => {
    vi.mocked(api.getLegislatorsBills).mockResolvedValue({ data: mockLegislatorsData } as any)
    
    render(
      <BrowserRouter>
        <Legislators />
      </BrowserRouter>
    )

    await waitFor(() => {
      expect(screen.getByText('1 - John Doe')).toBeInTheDocument()
      expect(screen.getByText('2 - Jane Smith')).toBeInTheDocument()
    })
  })

  it('displays "No legislators found" when there are no legislators', async () => {
    vi.mocked(api.getLegislatorsBills).mockResolvedValue({ data: [] } as any)
    
    render(
      <BrowserRouter>
        <Legislators />
      </BrowserRouter>
    )

    await waitFor(() => {
      expect(screen.getByText('No legislators found')).toBeInTheDocument()
    })
  })

  it('calls getLegislatorsBills on mount', async () => {
    vi.mocked(api.getLegislatorsBills).mockResolvedValue({ data: mockLegislatorsData } as any)
    
    render(
      <BrowserRouter>
        <Legislators />
      </BrowserRouter>
    )

    await waitFor(() => {
      expect(api.getLegislatorsBills).toHaveBeenCalledTimes(1)
    })
  })
})

