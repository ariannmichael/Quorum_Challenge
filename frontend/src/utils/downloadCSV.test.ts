import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest'
import { downloadCSV } from './downloadCSV'

// Mock global fetch
global.fetch = vi.fn()

describe('downloadCSV', () => {
  beforeEach(() => {
    vi.clearAllMocks()
    // Mock URL.createObjectURL and revokeObjectURL
    global.URL.createObjectURL = vi.fn(() => 'blob:mock-url')
    global.URL.revokeObjectURL = vi.fn()
    
    // Mock document.createElement and appendChild/removeChild
    const mockLink = {
      href: '',
      setAttribute: vi.fn(),
      click: vi.fn(),
    }
    vi.spyOn(document, 'createElement').mockReturnValue(mockLink as any)
    vi.spyOn(document.body, 'appendChild').mockImplementation(() => mockLink as any)
    vi.spyOn(document.body, 'removeChild').mockImplementation(() => mockLink as any)
  })

  afterEach(() => {
    vi.restoreAllMocks()
  })

  it('creates a download link and clicks it', async () => {
    const mockBlob = new Blob(['test,data'], { type: 'text/csv' })
    vi.mocked(global.fetch).mockResolvedValue({
      ok: true,
      blob: () => Promise.resolve(mockBlob),
    } as Response)

    await downloadCSV('/api/test.csv', 'test.csv')

    expect(global.fetch).toHaveBeenCalledWith('/api/test.csv')
    expect(document.createElement).toHaveBeenCalledWith('a')
  })

  it('handles fetch errors gracefully', async () => {
    const consoleSpy = vi.spyOn(console, 'error').mockImplementation(() => {})
    vi.mocked(global.fetch).mockRejectedValue(new Error('Network error'))

    // Should not throw
    await expect(downloadCSV('/api/test.csv', 'test.csv')).resolves.not.toThrow()
    
    expect(consoleSpy).toHaveBeenCalled()
    consoleSpy.mockRestore()
  })

  it('handles non-ok responses', async () => {
    const consoleSpy = vi.spyOn(console, 'error').mockImplementation(() => {})
    vi.mocked(global.fetch).mockResolvedValue({
      ok: false,
      status: 404,
    } as Response)

    // Should not throw, but should handle error
    await expect(downloadCSV('/api/test.csv', 'test.csv')).resolves.not.toThrow()
    
    expect(consoleSpy).toHaveBeenCalled()
    consoleSpy.mockRestore()
  })
})

