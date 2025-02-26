export interface Legislator {
  id: number;
  name: string;
}

export interface LegislatorBills {
  legislator: Legislator;
  supported_bills: number;
  opposed_bills: number;
}